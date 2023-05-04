document.addEventListener('DOMContentLoaded', function() {    

    document.querySelector('#newpost-form').addEventListener('submit', submit_post);

    // By default load the old posts
    load_post();
});

function submit_post(event) {
    event.preventDefault();

    // Store field from the post form
    let content = document.querySelector('#post-content').value;

    // Send a POST request to the URL
    fetch('/newpost', {
        method: 'POST',
        body: JSON.stringify({
            content: content,
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
    })
}

function load_post() {

    // Send a GET request to the URL
    fetch('/post')
    .then(response => response.json())
    .then(posts => {posts.forEach(post => {
        console.log(post);
        let element = document.createElement('div');
        element.style.border = "dashed"
        element.innerHTML = `${post.user}<br>${post.content}<br>${post.timestamp}<br>${post.like} like(likes)<br>`;
        document.querySelector('#post-view').append(element);
        });
    })
}

