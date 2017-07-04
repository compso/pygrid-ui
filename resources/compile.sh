
# The path to output all built .py files to: 
UI_PYTHON_PATH=../pygrid-ui/ui


# Helper functions to build UI files
function build_qt {
    echo " > Building " $2
    
    # compile ui to python
    $1 $2 > $UI_PYTHON_PATH/$3.py
}

function build_ui {
    build_qt "pyside2-uic --from-imports" "$1.ui" "$1"
}  

function build_res {
    build_qt "pyside2-rcc" "$1.qrc" "$1_rc"
}


# build UI's:
echo "building user interfaces..."
build_ui MainWindow
build_ui JobInfoDialog
# add any additional .ui files you want converted here!

# build resources
# echo "building resources..."
# build_res resources