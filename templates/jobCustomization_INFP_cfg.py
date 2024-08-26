import FWCore.ParameterSet.Config as cms

from input_cfg import process

process.maxEvents.input = cms.untracked.int32(TEMPL_NEVENTS)
process.source.fileNames = cms.untracked.vstring(TEMPL_INFILES)
process.out.fileName = cms.string('TEMPL_OUTFILE')

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(TEMPL_NCPU)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)
