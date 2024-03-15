#!/bin/bash

source params.sh

source /afs/cern.ch/user/c/cerminar/scripts/cmssetup.sh
export SCRAM_ARCH=${SCRAMARCH}
echo "Setup area for SCRAM_ARCH: ${SCRAM_ARCH}"
scram proj CMSSW ${CMSSWVERSION}
cd ${CMSSWVERSION}
cp ../sandbox.tgz .
tar xvf sandbox.tgz
ls -lrt

