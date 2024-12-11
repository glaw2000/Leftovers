let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

document.addEventListener('DOMContentLoaded', function() {
    // code below will now only run when the DOM is fully loaded
    document.getElementById('like-button').addEventListener('click', function() 
    {
        likePost(postSlug);
    });
});

// Function below sends a POST request to like a blog post identified by unique postslug that is passed in from post_detail.html.
// Fetch API makes HTTP request to the server.
// Each time like button is clicked function checks if element already has a class of 'liked' then removes it
// otherwise it sets class of 'liked' on element and increments like-count by one. The class of "clicked" also gets toggled to change the button color.

function likePost(slug) {
    fetch(`/blog/${slug}/like/`,{
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrfToken
        },
        body:JSON.stringify({}),
    })
    .then(response => {
        if(!response.ok) {
            return response.text().then(text=> {throw new Error(text);});
        }
        return response.json();
    })
    .then(data => {
        const likeButton = document.getElementById('like-button');
        if (data.liked) {
            likeButton.classList.add('liked');
        } else {
            likeButton.classList.remove('liked');
        }
        document.getElementById('like-count').textContent = data.like_count;
        
        // Toggle the button color
        likeButton.classList.toggle('clicked');
    })
    .catch(error => console.error('Error:', error));
}