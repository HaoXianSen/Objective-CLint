#!/usr/bin/env bash
# format-objc-file.sh
# Formats an Objective-C file, replacing it without a backup.
# Copyright 2015 harry, Inc

cat <<EOF
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8" />
    <!-- Make sure to load the highlight.js CSS file before the Diff2Html CSS file -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.1/styles/github.min.css" />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.jsdelivr.net/npm/diff2html/bundles/css/diff2html.min.css"
    />
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/diff2html/bundles/js/diff2html-ui.min.js"></script>
  </head>
  <script>
EOF

echo -n -e "const diffString = \`"
while IFS= read -r line; do
    echo -e "${line}"
done 
echo "\`"
echo -e "\n"

cat <<EOF
 document.addEventListener('DOMContentLoaded', function () {
      var targetElement = document.getElementById('myDiffElement');
      var configuration = {
        drawFileList: true,
        fileListToggle: true,
        fileListStartVisible: false,
        fileContentToggle: true,
        matching: 'lines',
        outputFormat: 'side-by-side',
        synchronisedScroll: true,
        highlight: true,
        renderNothingWhenEmpty: false,
      };
      var diff2htmlUi = new Diff2HtmlUI(targetElement, diffString, configuration);
      diff2htmlUi.draw();
      diff2htmlUi.highlightCode();
    });
  </script>
  <body>
    <div id="myDiffElement"></div>
  </body>
</html>
EOF
