function extract() {

    // 1. Get the data
    var data = document.evaluate('//*[@id="widecol"]/div/table', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

    // 2. Create a Blob object with the data
    var blob = new Blob([data], {type: 'text/plain'});

    // 3. Create a temporary link element
    var link = document.createElement('a');

    // 4. Create an object URL from the blob
    link.href = window.URL.createObjectURL(blob);

    // 5. Set the download attribute with a file name
    link.download = 'export_table_data.txt';

    // 6. Append the link to the document (not visible)
    document.body.appendChild(link);

    // 7. Programmatically trigger a click event on the link to download the file
    link.click();

    // 8. Remove the link from the document
    document.body.removeChild(link);
}