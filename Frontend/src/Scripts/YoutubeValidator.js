function validateYouTubeUrl(url) {
  // Regular expression to check the format of a YouTube URL
  const youtubeRegex =
    /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;

  // Test the URL against the regular expression
  if (youtubeRegex.test(url)) {
    // The URL is in a valid format
    return true;
  } else {
    // The URL is not in a valid format
    return false;
  }
}

export default validateYouTubeUrl;
