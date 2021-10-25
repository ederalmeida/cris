import cx_Freeze

build_exe_options = {
"include_msvcr": True
}

exe = [cx_Freeze.Executable("cris.py", base = "Win32GUI",
        target_name = "cris_v1.2.1.exe")]
cx_Freeze.setup(
    name = "CRIS v1.2.1",
    options = {"build_exe": build_exe_options},
    executables = exe
)
