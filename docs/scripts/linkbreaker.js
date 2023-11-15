function addWbrToLinks() {
    // Get all elements with anchor tags
    var links = document.getElementsByTagName('a');

    // Loop through each anchor tag
    for (var i = 0; i < links.length; i++) {
        var link = links[i];

        // Get the original link
        var originalLink = link.innerHTML;

        // Split the link by "/"
        var parts = originalLink.split('/');

        // Create a new link with <wbr> after each "/"
        var newLink = parts.join('/<wbr>');

        // Set the innerHTML of the anchor tag to the new link
        link.innerHTML = newLink;
    }
}