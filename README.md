# Alfred Icon Generator
Icon Generator quickly converts any SF Symbol to a .png file for use in Alfred workflows.

![SCR-20221001-2zf](https://user-images.githubusercontent.com/4795315/193312018-ed7c1ac4-087c-4abc-840c-6461cb2bf32b.png)

# Demonstration
https://user-images.githubusercontent.com/4795315/193312166-13437d6c-cf65-449a-99aa-427dff68be45.mp4

# Why I made this
I make extensive use of Alfred's List Filters to pop up various little context menus all over the place throughout my being on the computer. I like to include icons for many of these entries, for example, here is my Audio Hijack loudness adapted volume control popup menu:

![image](https://user-images.githubusercontent.com/4795315/192548164-a4684b48-8184-4777-9660-745fc7c47338.png)

So this is a solution to quikcly generate pretty and consistent icons.

# Dependencies: 
Must install ImageMagick first - `brew install imagemagick`

Must install SF-Pro-Display-Bold.otf from Apple - https://devimages-cdn.apple.com/design/resources/download/SF-Pro.dmg

# Configuraton
You can configure the icon colour as well as the location on disk where icons are generated (defaults to /tmp) 

# Operation
There's 2 ways to run the workflow: Through the clipboard or through Alfred's Universal Actions.

1. Clipboard method
Copy a single symbol to the clipboard then run the trigger. tada, your clipboard now has your new icon on it.

2. Universal Action method
Select a single symbol and execute the workflow through Alfred's univeral action feature. Again, tada.

# Credit
This workflow was adapted from code by Mark Gavin - https://labs.appligent.com/pdfblog/convert-sf-symbols-to-images/
This wouldn't be possible without the help of user Vitor from the Alfred forum. 
