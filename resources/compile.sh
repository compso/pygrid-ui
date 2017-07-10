
# The path to output all built .py files to: 
UI_PYTHON_PATH=../pygrid-ui/ui
ICON_PATH=png
SVG_PATH=svg


# Helper functions to build UI files
function build_qt {
    echo " > Building " $2
    
    # compile ui to python
    $1 $2 > $UI_PYTHON_PATH/$3.py
}

function build_ui {
    build_qt "pyside2-uic --from-imports" "$1.ui" "$1UI"
}  

function build_res {
    build_qt "pyside2-rcc" "$1.qrc" "$1_rc"
}


function build_icon {
	i=`basename $1`;
	echo " > Building $i.svg";
    inkscape -e $ICON_PATH/$i.png $1.svg;
}

# build UI's:
echo "building user interfaces..."
for ui in *.ui; do
	build_ui ${ui%.*};
done

# add any additional .ui files you want converted here!

echo "building icons..."
for ico in $SVG_PATH/*.svg; do
	build_icon ${ico%.*};
done

# build resources
echo "building resources..."
for qrc in *.qrc; do
	build_res ${qrc%.*};
done
