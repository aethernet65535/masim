from masim_config import Region, AccessPattern, Phase, pr_config
import numpy as np

KiB = 1 * 1024
MiB = 1024 * KiB
GiB = 1024 * MiB

SEC_MS = 1000
MIN_MS = 60 * SEC_MS

TOTAL_MEM = 8 * GiB
REGION_SZ = 1 * MiB
NR_REGION = TOTAL_MEM // REGION_SZ

TEST_TIME = 60 * MIN_MS
OPS = 24
ACCESS_TIME = SEC_MS // OPS
NR_ACCESS = TEST_TIME // ACCESS_TIME

ZIPF_ALPHA = 1.01

rng = np.random.default_rng()

def get_zipf_index(nr_region, a):
    index = rng.zipf(a, None)
    return (index - 1) % nr_region

regions = [
    Region(f'region_{i}', REGION_SZ, 'none')
    for i in range(NR_REGION)
]

phases = []

for i in range(NR_ACCESS):
    target_idx = get_zipf_index(NR_REGION, ZIPF_ALPHA)
    phases.append(Phase(f'scene1_zipf_{i}', ACCESS_TIME, [
        AccessPattern(f'region_{target_idx}', True, 0, 100, 'rw'),
    ]))

pr_config(regions, phases)
