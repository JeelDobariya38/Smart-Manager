// Note: Below code assume that the asset for windows attach to release will have nameing patten as `smart-manager.${release.tag}.zip`

const apiEndpoint = 'https://api.github.com/repos/JeelDobariya38/smart-manager/releases/latest';

function toggle_error_section(path) {
    var error_section = document.getElementById('error_section');
    
    if (path !== '#') {
        error_section.style.display = 'none';
    } else {
        error_section.style.display = 'block';
    }
}

function is_on_windows() {
    // Replace this logic with your actual platform detection logic
    const platformDropdown = document.getElementById('platformDropdown');
    return platformDropdown.value === 'windows';
}

const downloadButton = document.getElementById('downloadButton');

async function fetchLatestRelease() {
    try {
        const response = await fetch(apiEndpoint);
        const data = await response.json();

        if (response.ok) {
            const isWindows = is_on_windows();
            const downloadURL = isWindows ? getWindowsDownloadURL(data.assets, data.tag_name) : getSourceCodeDownloadURL(data.assets);
            console.log(downloadURL);
            window.location.href = downloadURL;
        } else {
            toggle_error_section('#');
            console.error('Failed to fetch latest release:', data.message);
        }
    } catch (error) {
        toggle_error_section('#');
        console.error('Error fetching latest release:', error);
    }
}

function getWindowsDownloadURL(assets, version) {
    const asset = assets.find(asset => asset.name.toLowerCase().includes(`smart-manager.${version}.zip`));
    const path = asset ? asset.browser_download_url : '#';
    toggle_error_section(path);
    return path;
}

function getSourceCodeDownloadURL(assets) {
    const asset = assets.find(asset => asset.name.toLowerCase().includes(`smart-manager.python.zip`));
    const path = asset ? asset.browser_download_url : '#';
    toggle_error_section(path);
    return path;
}

downloadButton.addEventListener('click', fetchLatestRelease);
