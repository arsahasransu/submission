#!/bin/bash

get_eos_protocol() {
    dirname=$1
    protocol=''

    if [[ $dirname == *'/eos/user/'* ]]; then
        protocol='root://eosuser.cern.ch/'
    elif [[ $dirname == *'/eos/cms/'* ]]; then
        protocol='root://eoscms.cern.ch/'
    fi

    echo $protocol
}

file_name_wprotocol() {
    filename=$1
    protocol=$(get_eos_protocol $filename)
    echo "${protocol}${filename}"
}

source job_info.sh

source params.sh

echo "CLUSTER:" ${CLUSTERID}
echo "PROC-ID" ${PROCID}
echo 'TASKCONFDIR' ${ABSTASKCONFDIR}
echo 'OUT-DIR' ${OUTDIR}
echo 'OUTPUT-FILE' ${OUTFILE}


BATCH_DIR=${PWD}
echo "Current dir: ${BATCH_DIR}"
ls -l

IFS=',' read -ra FILELIST <<< "$OUTFILE"

for OFILE in "${FILELIST[@]}"; do
    extension="${OFILE##*.}"
    filename="${OFILE%.*}"
    OUTTARGET="${OUTDIR}/${filename}_${CLUSTERID}_${PROCID}.${extension}"

    cp "${OFILE}" "${OUTTARGET}"
    if [ $? -eq 0 ]; then
        echo "Copy succeeded for ${OFILE}"
    else
        eos cp "$(file_name_wprotocol "${OFILE}")" "$(file_name_wprotocol "${OUTTARGET}")"
    fi
done
