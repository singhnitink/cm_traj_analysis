#!/bin/bash
vmd -dispdev text -e cm.tcl
echo "analysis done"
python3 cm_traj_analysis.py
echo "Contact map generated"
