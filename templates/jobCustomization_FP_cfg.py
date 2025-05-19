import FWCore.ParameterSet.Config as cms

from input_cfg import *

TEMPL_CUSTOMIZE

process.maxEvents.input = cms.untracked.int32(TEMPL_NEVENTS)
process.source.fileNames = cms.untracked.vstring(TEMPL_INFILES)
# process.outnano.fileName = cms.untracked.string('TEMPL_OUTFILE')

