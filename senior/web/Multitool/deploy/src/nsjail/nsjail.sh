#!/bin/bash

mkdir -p /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
mkdir -p /var/log/nsjail

nsjail \
    -Mo \
    --chroot /chroot/ \
    --user nobody \
    --group nogroup \
    --hostname jail \
    --time_limit 30 \
    --cgroup_cpu_ms_per_sec 100 \
    --cgroup_mem_max 8388608 \
    --cgroup_pids_max 16 \
    --disable_clone_newnet \
    -E PATH=/bin:/usr/bin \
    --verbose \
    -D app/ \
    -- $@
