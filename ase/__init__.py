# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.


import os 

ASE_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
"""Absolute path to the ASE repository."""

POSELIB_DIR = os.path.join(ASE_ROOT_DIR, "ase", "poselib")
"""Absolute path to the poselib repository."""
