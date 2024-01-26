# HuffmanTree-Compression
Efficient Huffman Tree Compression with a user-friendly web server for easy testing. The Huffman Tree algorithm reduces file sizes while maintaining data integrity.

Running the code:
Go to the wwwroot directory. Open a bash terminal and open the web server using "python3 ../webserver.py". You can then go to the url "http://localhost:8000" to view the webpage and image of Huffman that will appear if the decompressor is functioning properly. Note that the port can be changed by modifying the variable port in webserver.py.

To compress a file, first copy that file over to the wwwroot directory and then move to that directory and type "python3 ../compress.py somefile.ext" where somefile is the name of the file you wish to compress and ext is the extension. Then go to the url "http://localhost:8000/somefile.ext" to view and/or download the decompressed file.
