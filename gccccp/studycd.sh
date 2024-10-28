#!/bin/sh
# begin linux programmer page70

menu_choice=""
curent_cd=""
title_file="title.cdb"
tracks_file="tracks.cdb"
# 2 files save data
temp_file=/tmp/cdb.$$
trap 'rm -f $temp_file' EXIT
# del before exit 0;

get_return(){
    echo -e " Press return \c"
    read x
    return 0
}

get_confirm(){
    echo -e " Are you sure? \c"
    while true
    do
        read x
        case "$x" in 
            y | yes | Y | Yes | YES ) return 0;;
            n | no  | N | No | NO ) 
                echo 
                echo " Canceled ! "
                return 1;;
            * ) echo " Please enter yes or no! ";;
        esac
    done
}

set_menu_choice(){
    clear
    echo " Options :---"
    echo 
    echo " a) Add new CD "
    echo " f) Find  CD "
    echo " s) Show all CDs "
    echo " c) Count CDs and tracks in the catalog  "
    if [ "$cdcatnum" != "" ]; then
        echo " l) List tracks on $cdtitle "
        echo " r) Remove $cdtitle "
        echo " u) Update track information for $cdtitle "
    fi
    echo " q) Quit"
    echo 
    echo -e "Pleast enter choice the press return \c"
    read menu_choice
    return
}

insert_title(){
    echo $* >> $title_file
    return
}

insert_track(){
    echo $* >> $tracks_file
    return
}

add_record_tracks(){
    echo " Enter track information for this CD "
    echo " When no more tacks enter q! "
    cdtrack=1
    cdttitle=""
    while [ "$cdttitle" != "q" ]
    do
        echo -e " Track $cdtrack , track title? \c"
        read tmp
        cdttitle=${tmp%%,*}
        if [ "$tmp" != "$cdttitle" ]; then
            echo "Sorry, no commas allowed "
            continue
        fi
        if [ -n "$cdttitle" ]; then
            if [ "$cdttitle" != "q" ]; then
                insert_track $cdcatnum,$cdtrack,$cdttitle
            fi
        else
            cdtrack=$((cdtrack-1))
        fi 
    cdtrack=$((cdtrack+1))
    done
}

add_records(){
    echo -e " Enter catalog name \c"
    read tmp
    cdcatnum=${tmp%%,*}
    echo -e " Enter title \c "
    read tmp
    cdtitle=${tmp%%,*}
    echo -e " Enter type \c "
    read tmp
    cdtype=${tmp%%,*}
    echo -e " Enter artist/composer  \c "
    read tmp
    cdac=${tmp%%,*}
    
    echo "About to add new entry"
    echo " $cdcatnum $cdtitle $cdtype $cdac "
    if get_confirm ; then 
        insert_title $cdcatnum, $cdtitle, $cdtype, $cdac 
        add_record_tracks
    else 
        remove_records
    fi
    return 
}

find_cd(){
    echo " find..."
    if [ "$1" = "n" ]; then 
        asklist=n
    else
        asklist=y
    fi
    cdcatnum=""
    echo -e " Enter a string to search for in the CD titles \c"
    read searchstr
    if [ "$searchstr" = "" ]; then 
        return 0
    fi
    grep "$searchstr" $title_file > $temp_file
    set $(wc -l $temp_file)
    linesfound=$1

    case "$linesfound" in 
    0 ) echo " Sorry, nothing found!"
        get_return
        return 0
        ;;
    1 ) ;;
    2 ) echo " Sorry, not unique."
        echo " Found the following:"
        cat $temp_file
        get_return
        return 0
    esac

    IFS=","
    read cdcatnum cdtitle cdtype cdac < $temp_file
    IFS=" "

    if [ -z "$cdcatnum" ]; then 
        echo " Sorry, could not extra catalog field from $temp_file"
        get_return
        return 0
    fi

    echo
    echo Catalog number: $cdcatnum
    echo Title: $cdtitle
    echo Type: $cdtype
    echo Artist/Composer: $cdac
    echo 
    get_return

    if [ "$asklist" = "y" ]; then
        echo -e " Views tracks for this cd? \c"
        read x
        if [ "$x" = "y" ]; then
            echo
            list_tracks
            echo
        fi
    fi
    return 1
}

update_cd(){
    echo " update..."
    return 0
}


count_cds(){
    set $(wc -l $title_file)
    num_titles=$1
    set $(wc -l $tracks_file)
    num_tracks=$1
    echo found $num_titles CDs with a total of $num_tracks tracks
    get_return
    return
}



remove_records(){
    echo " remove..."
    return 
}
list_tracks(){
    if [ "$cdcatnum" = "" ]; then 
        echo no CD select yet
        return
    else
        grep "^${cdcatnum}," $tracks_file > $temp_file
        set =$(wc -l $temp_file)
        num_tracks=$1
        if [ "$num_tracks" = "0" ]; then
            echo no tracks found for $cdtitle
        else {
            echo 
            echo "$cdtitle :----->"
            echo 
            cut -f 2- -d , $temp_file
            echo 
        } | ${PAGER:-more}
        fi
    fi
    get_return
    return
}

show_cds(){
    set $(wc -l $title_file)
    num_cd=$1
    if [ "$num_cd" = "0" ]; then
        echo no CD found in database
    else {
        echo
        echo " There are  $num_cd CDS in this list : "   
        echo catalog title type artist/composer
        echo ----------------------------------
        cat $title_file
        echo 
    } | ${PAGER:-more}
    fi
    get_return
    return
}

#main()
rm -f $temp_file
if [ ! -f $title_file ]; then
    touch $title_file
fi
if [ ! -f $tracks_file ]; then
    touch $tracks_file
fi
clear
echo 
echo
echo "-------Mini CD manager----------"

quit=n
while [ "$quit" != "y" ];
do
    set_menu_choice
    case "$menu_choice" in
        a) add_records;;
        r) remove_records;;
        f) find_cd;;
        s) show_cds;;
        u) update_cd;;
        c) count_cds;;
        l) list_tracks;;
        b)
            echo
            more $title_file
            echo 
            get_return;;
        q | Q ) quit=y;;
        * ) echo " Sorry, choice not recongnized!";;
    esac
done

rm -f $temp_file
echo "Finshed! \c"
exit 0


        





























:<<!
#####################test func
yes_or_no() {
    echo "is this you name $* ?"
    while true
    do
        echo -n "Enter yes or no: "
        read x
        case "$x" in 
            y | Y | yes ) return 0;;
            n | N | no  ) return 1;;
            * ) echo "answer yes or no!"
        esac
    done
}

echo " sh file is start"
echo " original parameters are $*"
if yes_or_no "$1"
then 
    echo "Hi $1, nice name"
else 
    echo "no name input"
fi
exit 0
!





:<<!
#####################test case
echo "input yes or no : "
read myinput
case "$myinput" in 
    yes | y | Y | YES ) echo "you input yes";;
    no | n | N | NO ) echo "you input no";;
    * ) echo "you input is not yes or no!";;
esac
exit 0
!





:<<!
#####################test case
echo "what time is it? please input:"
read inputtime
case "$inputtime" in 
    12 ) echo "It is 12 o'clock " ;;
    11 ) echo "It is 11 o'clock " ;;
    10 ) echo "It is 10 o'clock " ;;
    yes ) echo "input a number,you input yes? " ;;
    no ) echo "input a number, you input no?" ;;
    * )  echo "error,quit";;
esac
exit 0
!


:<<!
#####################test until:
# $1 为第一个参数
until who | grep "$1" >/dev/null
do
    sleep 60
done

echo -e '\a'
echo "**** $1 has just logged in ****"
!



:<<!
#####################test while:
echo "enter password: "
read pass
while [ "$pass" != "password" ]; 
do
    echo "input password is error,try again:"
    read pass
done
echo "password is \"password\"!"
exit 0
!


:<<!
#####################test for:
for i in bar fud 234
do 
    echo $i
done

for filename in $(ls *.sh); 
do 
    echo $filename
done

!


:<<!
echo "Is it morning? Please answer yes or no: "
read timeofday

if    [ "$timeofday" = "yes" ]; then
    echo "good morning"
elif  [ "$timeofday" = "no" ] ; then
    echo "good afternoon"
else
    echo "sorry, please enter yes or no, input  error!"
    exit 1
fi
!

