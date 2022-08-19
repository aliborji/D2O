
for f in *; do

	rm $f/*.gif
	rm $f/*.svg


	a=1
	for i in $f/*; do
	  new=$(printf "%04d.jpeg" "$a") #04 pad to length of 4
	  mv -i -f -- "$i" "$f/$new"
	  let a=a+1
	done

	ls $f/* | wc -l
	ls $f/*.jpeg | wc -l

done


find . -maxdepth 2 -type f | wc -l