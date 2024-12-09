let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value

document.getElementById('like-button').addEventListener('click', function() {
    likePost(postSlug);
});

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
            return response.text().then(text=> {throw new Error(text)});
        }
        return response.json();
    })
    .then(data => {
        if (data.liked) {
            document.getElementById('like-button').classList.add('liked');
        } else {
            document.getElementById('like-button').classList.remove('liked');
        }
        document.getElementById('like-count').textContent = data.like_count;
    })
    .catch(error => console.error('Error:',error));
}