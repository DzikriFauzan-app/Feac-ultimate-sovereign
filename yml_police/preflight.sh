#!/bin/sh
python yml_police/yml_police.py buildozer.spec || {
  echo "[PRE-FLIGHT] BUILD DIBATALKAN"
  exit 1
}
echo "[PRE-FLIGHT] AMAN — LANJUTKAN BUILD MANUAL"
