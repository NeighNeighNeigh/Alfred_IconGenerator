# Alfred Icon Generator
This workflow will convert a single Emoji or SF Symbol to an icon (png file) and place it on the clipboard. Handy for adding icons to your Alfred workflows. 

<img width="1427" alt="image" src="https://github.com/NeighNeighNeigh/Alfred_IconGenerator/assets/4795315/c707bc5a-cb07-441b-bb1f-822c62210c5f">


## Dependencies: 
 - SF Symbols - https://developer.apple.com/sf-symbols/
 - ImageMagick (available via Homebrew)
 - Pillow for Python (available via Homebrew)

(Note: the latter two dependencies can be handled by Alfred if you are installing through the [Alfred Gallery](https://alfred.app/workflows/floatingpoint/icon-generator/))

## Configuration
In the workflow's configuration you can adjust the SF Symbol weight, colour and background settings, as well as define the location on disk where icons are generated (defaults to /tmp) 

## There's 2 ways to run the workflow

### 1. Clipboard method

Copy either a single symbol from SF symbols, or a single emoji to the clipboard. Now run the trigger. The workflow has converted the source into a png image and copied it to your clipboard - ready to paste into any icon field within Alfred (or wherever you like).

### 2. Universal Action method

Select a single symbol / emoji and execute the workflow through Alfred's univeral action feature.


## Acknowledgements

The SF Symbols portion of this workflow was adapted from work by Mark Gavin - https://labs.appligent.com/pdfblog/convert-sf-symbols-to-images/

This wouldn't be possible without the help of user Vitor from the Alfred forum. 
