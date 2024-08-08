from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TEMPL_REQUESTNAME'
config.Data.inputDataset = 'TEMPL_INPUTDATASET'
config.Data.partialDataset = True

config.General.workArea = 'TEMPL_TASKDIR'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TEMPL_TASKCONFDIR/input_cfg.py'
config.JobType.maxMemoryMB = 4000
# config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 7000

config.Data.inputDBS = 'global'
config.Data.splitting = 'TEMPL_SPLITTINGMODE'
config.Data.unitsPerJob = TEMPL_SPLITGRANULARITY
config.Data.totalUnits = TEMPL_NEVENTS
config.Data.outLFNDirBase = 'TEMPL_CRABOUTDIR'
config.Data.publication = False
config.Data.ignoreLocality = False
config.Data.outputDatasetTag = 'TEMPL_DATASETTAG'

config.Site.storageSite = 'TEMPL_STORAGE'
config.JobType.allowUndistributedCMSSW = True
