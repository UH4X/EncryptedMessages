# EncryptedMessages
I have made this cipher tool for fun, but you can add an ID that is so large that  it'll be basically impossible to decrypt unless the other part has that same exact ID that you used to encrypt with.


Let's say you have this message: "Hello how are you doing today?" but you want nobody to know what that message includes except the other part you are going to send it to, then you can write any
Range-ID that you'd like. So let's just say for fun a Range-ID of "999999999999999999" then that is the key to decrypt the message which you would want to give to the other part who has to know about
this encrypted message that YOU are sending. (This can also be reverse so not just you sending to another part, but the part can send to you also).

There is a help commandline in there. To see what you can do just write "help" when in the prompt.

Pro tip: You need python (Tested only on: 3.12.8) for this to work✌️

Edit on: 15th December 2024
Also I know that when this program, file or release is downloaded, it'll say that it's a virus, but it's really not.
The reason it says it's a virus is because of the "import os" library where I have used "os.system('cls')" to clear the screen and make everything look nicer.
But that apparently gets flagged which I didn't know. I asked ChatGPT why and it's telling me to use subprocess, so I'll take a look at that later.

Edit on: 16th December 2024
If your file still flags in v1.2 then I really don't know why or how to fix it. It's a false positive, Here is a TotalVirus Scanning: https://www.virustotal.com/gui/file/7cc04074581b4fb6d7de017eef68f3363640ad0423dbfa46cd8b1b3ea39702d1

Also I asked ChatGPT which may be able to give you a better understanding of why this program flags. Here is my conversation with it:
https://chatgpt.com/share/67602818-e47c-800b-91e5-76947a655bba

If you still don't want to take the "risk" of potential virus, then it's fully understood. You may have a continued good day;)
