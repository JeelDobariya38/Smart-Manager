/* requires <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/2.0.3/marked.min.js"></script> */
/* requires <script src="{root-of-repo}/docs/scripts/linkbreaker.js"></script> */
// Note: Below code assume that the asset for windows attach to release will have nameing patten as `smart-manager.${release.tag}.${platform}.zip`

document.addEventListener("DOMContentLoaded", function () {
    // Ensure marked.js is loaded
    if (typeof marked === 'undefined') {
        console.error("marked.js is not loaded");
        return;
    }

    fetch("https://api.github.com/repos/JeelDobariya38/Smart-Manager/releases")
        .then(response => response.json())
        .then(releases => {
            console.log(releases);

            // Find the "Other Releases" container
            const otherReleasesContainer = document.querySelector('.other-version');
            console.log(otherReleasesContainer)

            for (var release of releases) {
                if (!release.draft) {
                    var convertedBody = marked(release.body); // <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/2.0.3/marked.min.js"></script>
                    var pythondownloadlink = '#';
                    var windowsdownloadlink = '#';
                    for (var asset of release.assets) {
                        if (asset.name.endsWith(".zip")) {
                            if (asset.name.endsWith("python.zip")) {
                                pythondownloadlink = asset.browser_download_url;
                            }
                            if (asset.name.endsWith("windows.zip")) {
                                windowsdownloadlink = asset.browser_download_url;
                            }
                        }
                    }
                    var releaseElement = document.createElement('div');
                    releaseElement.classList.add('release');
                    releaseElement.innerHTML = `
                        <h1>${release.name}</h1>
                        <div class="info">
                            <div><b>Prerelease: <span class="prerelease">${release.prerelease}</span></b></div>
                            <div><b>Published At: <span class="published-at">${release.published_at}</span></b></div>
                        </div>
                        <div class="notes">${convertedBody}</div>
                        <a class="ignore" href="${pythondownloadlink}" target="_blank"><button class="downloadbtn">Python Download</button></a>
                        <a class="ignore" href="${windowsdownloadlink}" target="_blank"><button class="downloadbtn">Windows Download</button></a>
                    `;
                    otherReleasesContainer.appendChild(releaseElement);
                }
            }

            // Check if there are no other releases and display an error message
            if (otherReleasesContainer.children.length === 0) {
                const errorMsg = document.querySelector('.other-version .error-msg');
                errorMsg.style.display = 'block';
            }

            addWbrToLinks(); // <script src="{root-of-repo}/docs/scripts/linkbreaker.js"></script>
        })
        .catch(error => console.error("Error fetching latest release:", error));
});
