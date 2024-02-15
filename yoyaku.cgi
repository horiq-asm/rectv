#!/bin/bash
echo "Content-type:text/html"
echo ""
echo "<head>"
echo "<meta charset=\"UTF-8\">"
echo "</head>"
read -r post_data
DECODED_DATA=$(echo "$post_data" | sed 's/+/ /g;s/%/\\x/g;' | xargs -0 printf "%b")
#echo "POSTされたデータ: $DECODED_DATA"
echo "<br>"
IFS='&' read -ra  parts <<< "$DECODED_DATA"
for part in "${parts[@]}"; do
    IFS='=' read -r key value <<< "$part "
    input_string+=$value
#    echo -n "$value ">>input_string
done
#echo "$input_string"
modified_string="${input_string:0:4} ${input_string:5:2} ${input_string:8:2} ${input_string:11:2} ${input_string:14}"
echo -n   "$modified_string">>/var/www/html/phot/rr.txt
echo '00'>>/var/www/html/phot/rr.txt
echo "<br>"
FILE_NAME=/var/www/html/phot/rr.txt
while read line;
do
  echo "${line}"
  echo "<br>"
done < /var/www/html/phot/rr.txt
