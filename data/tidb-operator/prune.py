import sys

sys.path.append('../..')
import input

custom_fields = [
    input.CopiedOverField(['spec', 'affinity']),
    input.OverSpecifiedField(['spec', 'discovery', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'discovery', 'additionalVolumes'], True),
    input.OverSpecifiedField(['spec', 'discovery', 'initContainers'], True),
    input.CopiedOverField(['spec', 'discovery', 'affinity']),
    input.CopiedOverField(['spec', 'discovery', 'tolerations'], True),
    input.CopiedOverField(['spec', 'discovery', 'podSecurityContext']),
    input.OverSpecifiedField(['spec', 'pd', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'pd', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'pd', 'affinity']),
    input.OverSpecifiedField(['spec', 'pd', 'initContainers'], True),
    input.CopiedOverField(['spec', 'pd', 'tolerations'], True),
    input.CopiedOverField(['spec', 'pd', 'podSecurityContext']),
    input.CopiedOverField(['spec', 'podSecurityContext']),
    input.OverSpecifiedField(['spec', 'pump', 'additionalContainers'], True),
    input.CopiedOverField(['spec', 'pump', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'pump', 'affinity']),
    input.CopiedOverField(['spec', 'pump', 'initContainers'], True),
    input.CopiedOverField(['spec', 'pump', 'tolerations'], True),
    input.CopiedOverField(['spec', 'pump', 'podSecurityContext']),
    input.OverSpecifiedField(['spec', 'ticdc', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'ticdc', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'ticdc', 'affinity']),
    input.CopiedOverField(['spec', 'ticdc', 'initContainers'], True),
    input.CopiedOverField(['spec', 'ticdc', 'tolerations'], True),
    input.CopiedOverField(['spec', 'ticdc', 'podSecurityContext']), 
    input.OverSpecifiedField(['spec', 'tidb', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'tidb', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'tidb', 'affinity']),
    input.OverSpecifiedField(['spec', 'tidb', 'initContainers'], True),
    input.CopiedOverField(['spec', 'tidb', 'tolerations'], True),
    input.CopiedOverField(['spec', 'tidb', 'podSecurityContext']),
    input.OverSpecifiedField(['spec', 'tiflash', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'tiflash', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'tiflash', 'affinity']),
    input.CopiedOverField(['spec', 'tiflash', 'initContainers'], True),
    input.CopiedOverField(['spec', 'tiflash', 'tolerations'], True),
    input.CopiedOverField(['spec', 'tiflash', 'podSecurityContext']),
    input.OverSpecifiedField(['spec', 'tikv', 'additionalContainers'], True),
    input.OverSpecifiedField(['spec', 'tikv', 'additionalVolumes'], True),
    input.CopiedOverField(['spec', 'tikv', 'affinity']),
    input.OverSpecifiedField(['spec', 'tikv', 'initContainers'], True),
    input.CopiedOverField(['spec', 'tikv', 'tolerations'], True),
    input.CopiedOverField(['spec', 'tikv', 'podSecurityContext']),
    input.CopiedOverField(['spec', 'tolerations'], True)
]
