
项目环境
1. 安装 python3.9
2. 配置虚拟环境
    python3.9 -m venv mfe_venv_09
    激活虚拟环境 (Mac):
        source mfe_venv_09/bin/activate
    激活虚拟环境 (Windows)
        mfe_venv_09\Scripts\activate
    x deactivate
3. 安装所有依赖包
    pip install -r requirements.txt
    brew install tcl-tk
4. pyinstaller 打包命令:
    pyinstaller ./main.spec


开发常用命令:
# save dependent
pip freeze > requirements.txt


TODO:
update core
package exe file


