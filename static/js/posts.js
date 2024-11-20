document.addEventListener('DOMContentLoaded', function () {
    // Function to check and show the "Read More" link if needed
    function checkCaptions() {
        document.querySelectorAll('.post-caption').forEach(function (caption) {
            const lineHeight = parseInt(window.getComputedStyle(caption)
            .lineHeight); // Get the line-height of the caption
            const maxTwoLineHeight = lineHeight * 2; // Calculate the maximum height for 2 lines

            // If the actual height of the caption exceeds 2 lines, show the read-more link
            const postId = caption.id.split('-')[
            1]; // Extract the post ID from the caption element's id
            const readMoreLink = document.getElementById(`read-more-${postId}`);

            if (caption.scrollHeight > maxTwoLineHeight) {
                readMoreLink.style.display = 'inline'; // Show the Read More link
            } else {
                readMoreLink.style.display = 'none'; // Hide the Read More link if it's not needed
            }
        });
    }

    // Initial check when the page loads
    checkCaptions();

    // Recheck when the window is resized (throttled to avoid performance issues)
    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            checkCaptions();
        }, 250); // Delay of 250ms to throttle the resize event
    });
});

function toggleCaption(postId) {
    // Get the post caption and the read-more link by ID
    const caption = document.getElementById(`caption-${postId}`);
    const readMoreLink = document.getElementById(`read-more-${postId}`);

    // Toggle the 'expanded' class to show or hide full caption
    if (caption.classList.contains('expanded')) {
        caption.classList.remove('expanded');
        readMoreLink.innerHTML = "Read more"; // Switch to "Read more"
    } else {
        caption.classList.add('expanded');
        readMoreLink.innerHTML = "Read less"; // Switch to "Read less"
    }
}

// Toggle fucntion to show the comment section
function toggleComments(postId) {
    const comments = document.getElementById(`comments-${postId}`);
    if (comments.style.display === 'none' || !comments.style.display) {
        comments.style.display = 'block';
    } else {
        comments.style.display = 'none';
    }
}

// Functionality for the edit comment form.
document.addEventListener('DOMContentLoaded', function () {
    // Add click event for edit links
    document.querySelectorAll('.edit-comment-link').forEach(function (link) {
        link.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            document.getElementById(`comment-body-${commentId}`).style.display = 'none'; // Hide the comment text
            document.getElementById(`edit-comment-form-${commentId}`).style.display = 'block'; // Show the form
        });
    });

    // Add click event for cancel buttons
    document.querySelectorAll('.cancel-edit').forEach(function (button) {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            document.getElementById(`comment-body-${commentId}`).style.display = 'block'; // Show the comment text
            document.getElementById(`edit-comment-form-${commentId}`).style.display = 'none'; // Hide the form
        });
    });
});