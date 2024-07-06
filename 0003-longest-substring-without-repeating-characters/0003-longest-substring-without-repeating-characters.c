int lengthOfLongestSubstring(char* s) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }

    if (n == 0) return 0;

    int maxLength = 0;
    int start = 0;
    int charIndex[128];  // Assuming ASCII characters

    // Initialize all elements of charIndex to -1
    for (int i = 0; i < 128; i++) {
        charIndex[i] = -1;
    }

    for (int end = 0; end < n; end++) {
        // If the character is found again within the current window, move the start pointer
        if (charIndex[s[end]] >= start) {
            start = charIndex[s[end]] + 1;
        }

        // Update the last index of the character
        charIndex[s[end]] = end;

        // Calculate the length of the current window and update maxLength if necessary
        int currentLength = end - start + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }

    return maxLength;
}
