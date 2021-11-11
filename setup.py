import cx_Freeze
from apoio import versao_atual as versao

build_exe_options = {
"include_msvcr": True
}

exe = [cx_Freeze.Executable("cris.py", base = "Win32GUI",
        target_name = "cris_" + versao.v + ".exe")]
cx_Freeze.setup(
    name = "CRIS" + versao.v,
    options = {"build_exe": build_exe_options},
    executables = exe
)
