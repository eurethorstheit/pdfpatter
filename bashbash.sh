#!/bin/sh
PCHANGED=${2%.*}\_changed.pdf
PTEMP=${PCHANGED%.*}\_temp.pdf
PUNDO=${PCHANGED%.*}\_undo.pdf

if [ "$1" = "pfad" ]
then 
	cp $2 $PCHANGED
	evince $PCHANGED &
	exit
elif [ "$1" = "rotation" ]
then	
cp $PCHANGED $PUNDO
	if [ "$3" = "rechts" ]	
	then
		pdf270 $PCHANGED --outfile $PTEMP 
	elif [ "$3" = "links" ]	
	then	
	 	pdf90 $PCHANGED --outfile $PTEMP
	elif [ "$3" = "invert" ]	
	then	 	
	pdf180 $PCHANGED --outfile $PTEMP
	else
		echo "Nichts gewählt"
	fi
	cp $PTEMP $PCHANGED
	echo "Rotation erfolgreich"	
	exit
elif [ "$1" = "schneiden" ]
then
	cp $PCHANGED $PUNDO 	
	pdfjam --trim $3'cm '$4'cm '$5'cm '$6'cm' --clip true $PCHANGED --outfile $PTEMP
	cp $PTEMP $PCHANGED
	echo "Schneiden erfolgreich"	
	exit
elif [ "$1" = "undo" ]
then
	cp $PUNDO $PCHANGED  
	echo "UNDO erfolgreich"	
	exit
elif [ "$1" = "scale" ]
then
	cp $PCHANGED $PUNDO 	
	pdfjam --scale $3 --clip true $PCHANGED --outfile $PTEMP
	cp $PTEMP $PCHANGED
	echo "Skalieren erfolgreich"	
	exit
	echo "Dies hätte nicht angezeigt werden dürfen"
elif [ "$1" = "fertig" ]
then
	cp $PCHANGED $3  
	echo "Speichern erfolgreich"		
	exit
elif [ "$1" = "ende" ]
then
	rm $PCHANGED $ROTATED $PTEMP $PUNDO			
	echo "Auf wiedersehen"		
	exit
elif [ "$1" = "bookmarks" ]
then
	if [ "$3" = "bearbeiten" ]	
	then
		echo "Bearbeiten gewählt"	
		if [ -f $4 ]	
		then
			echo "Vorhanden"
			gedit $4&		
		else
			touch $4
			gedit $4&			
			echo "Nicht vorhanden"
		fi
	elif [ "$3" = "vorbereiten" ]
	then
		echo "Vorbereiten gewählt"
		rm $5
		touch $5		
		while read line           
			do           
			  TITEL=$(echo $line|cut -f1 -d";")        
			  SEITE=$(echo $line|cut -f2 -d";")
				echo ['/Title ('$TITEL') /Page '$SEITE' /OUT pdfmark' >> $5
			done <$4
		gedit $5
	elif [ "$3" = "bookmarken" ]
	then		
		gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile="$5_bm" pdfmarks&
#		gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile="$5" $2 $4 &
	else
		echo "Nichts gewählt"
	fi
exit
elif [ "$1" = "sortieren" ]
then
	cp $PCHANGED $PUNDO
	pdftk A=$3 B=$4 shuffle A B output $PCHANGED
	exit
elif [ "$1" = "seite_weg" ]
then
	echo $PCHANGED 	
	cp $PCHANGED $PUNDO
	DAVOR=$(($3-1))
	DANACH=$(($3+1))
	if [ "$3" = "1" ]
	then
		pdftk $PCHANGED \cat $DANACH"-end" output $TEMP"danach"
		cp $TEMP $PCHANGED
	else		
		pdftk $PCHANGED \cat "1-"$DAVOR output $PTEMP"davor"
		pdftk $PCHANGED \cat $DANACH"-end" output $PTEMP"danach"
		pdftk $PTEMP"davor" $PTEMP"danach" output $PCHANGED
	fi	
	rm $PTEMP"davor" $PTEMP"danach"
	exit
elif [ "$1" = "seite_mitte" ]
then
	pdftk $CHANGED dump_data|grep PageMediaDimensions|tail -1l|cut -c 22-28
	
else
	echo 'was anderes gewählt'
	exit
fi




