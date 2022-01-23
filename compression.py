import zipfile
zip = zipfile.ZipFile('compfiles.zip','w')
zip.write('texte.txt')
zip.write('texte.sha')
zip.close()
