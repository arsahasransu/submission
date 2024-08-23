import FWCore.ParameterSet.Config as cms

from TEMPL_ROOTCFG import process


process.source.fileNames = cms.untracked.vstring(TEMPL_INFILES)
## Events and lumi blocks
process.maxEvents.input = cms.untracked.int32(TEMPL_NEVENTS)

## Scramble
# import random
# rnd = random.SystemRandom()
for X in process.RandomNumberGeneratorService.parameterNames_(): 
   if X != 'saveFileName': getattr(process.RandomNumberGeneratorService,X).initialSeed = cms.untracked.uint32(TEMPL_SEED)
# 
process.FEVTDEBUGHLToutput.fileName = cms.untracked.string('file:TEMPL_OUTFILE')

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(TEMPL_NCPU)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)
