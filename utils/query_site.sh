#!/bin/bash

# Specify the dataset path
dataset_path="/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD"

# Use dasgoclient to query all blocks for the blocks in the dataset
blocks_info=$(dasgoclient --query="block dataset=${dataset_path}")

# Extract site information from the results
blocks=$(echo "$blocks_info" |  cut -d'"' -f4 | sort -u)




# Print the list of blocks
echo "blocks for dataset: ${dataset_path}"
echo "$blocks"


 Print the list of blocks
echo "blocks for blocks in dataset: ${dataset_path}"

# Loop over each site
for block in $blocks; do
    echo "Processing site: $block"
    site_info=$(dasgoclient --query="site block=${block}")
    echo "$site_info"
done
