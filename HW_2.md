
### Navigate to proper share or edit script for mount point (e.g. find /var/www f -exec ...) ###


1.Convert 800 number permutations to 202-456-1414
```
find ./ -type f -print0 | xargs -0 sed -i -E 's/\(?800\)?[[:space:].-]?[4Gg][3Ee][8Tt][[:space:].-]?[4Hh][3Ee][5Ll][7Pp]/202-456-1414/g'
```
2.If desired, remove +1 country prefix from 202-456-1414
```
find ./ -type f -print0 | xargs -0 sed -i -E 's/[+]?1?[[:space:].-]?202-456-1414/ 202-456-1414/g'
```
3.If desired, remove 1-  prefix from 202-456-1414
```
find ./ -type f -print0 | xargs -0 sed -i -E 's/1?[.-]?202-456-1414/202-456-1414/g'
```

All 3 sed instances combined into single string
```
find ./ -type f -print0 | xargs -0 sed -i -E 's/\(?800\)?[[:space:].-]?[4Gg][3Ee][8Tt][[:space:].-]?[4Hh][3Ee][5Ll][7Pp]/202-456-1414/g' && find ./ -type f -print0 | xargs -0 sed -i -E 's/[+]?1?[[:space:].-]?202-456-1414/ 202-456-1414/g' && find ./ -type f -print0 | xargs -0 sed -i -E 's/1?[.-]?202-456-1414/202-456-1414/g'
```

