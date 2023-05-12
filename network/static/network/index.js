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
        element.style.border = "dotted";
        // element.setAttribute("id", "show-post");
        // let element1 = document.createElement('div')
        // element1.innerHTML = `${post.username}`;
        // document.querySelector('#show-post').append(element1);
        element.innerHTML = `<a href="/profile/${post.user_id}">${post.username}</a><br>${post.content}<br>${post.timestamp}<br>${post.like} like(likes)<br>`;
        // show_post(post.username)
        // `${post.username}<br>${post.content}<br>${post.timestamp}<br>${post.like} like(likes)<br>`;
        // post.content, post.timestamp, post.like
        document.querySelector('#post-view').append(element);
        });
    })
}

function show_post(username) {
    let element_user = document.createElement('div');
    element_user.innerHTML = username;
    document.querySelector('#show-post').append(element_user);
}

