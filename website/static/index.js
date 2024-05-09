function deleteNote(noteId) {
    fetch('/delete-note',{
    method: 'POST',
    body :JSON.stringify({ noteId: noteId}),
    }).then((_res)=>{
        window.location.href = "/";
    });
}
// it takes the noteid passed then it sends POST request to note delete endpoint,
// after it gets a response frmo delete note endpoint, it will reload window
