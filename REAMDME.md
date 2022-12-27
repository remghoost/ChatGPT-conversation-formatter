# ChatGPT conversation reformatter for use in Pastebin

This tool is for reformatting an entire ChatGPT conversation into something that is actually readable in Pastebin (or anywhere else you'd want to use it).

It removes your email address and inserts lines between each message.

## Usage

Copy from your "icon" down to the end of the conversation.

Paste entire contents into text box.

**Your email address should be the first line.**

Press reformat button.

Output is saved in the same directory as the script

## Requirements
A working install of python.

## Installation
```
pip install -r requirements.txt
```
then use 
```
python reformat_conversation.py
```

## BUT ARE YOU STEALING MY EMAIL ADDRESS?!
Just wanted to hedge this one off at the pass because I know how the internet works.

I want nothing to do with your email address. Due to how the conversations are formatted in the HTML of the chat window, your email address is present on every response.

I can understand why they might want this, but I'm not a fan of blasting my email address all over a pastebin.

This script is 63 lines of code. Go read through it if you're scared of me somehow skimming info off of your computer.

## License

[MIT](https://choosealicense.com/licenses/mit/)