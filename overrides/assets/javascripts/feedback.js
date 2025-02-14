document$.subscribe(() => {
  const feedback = document.forms.feedback;

  if (!feedback) return;

  feedback.hidden = false;

  feedback.addEventListener('submit', function (event) {
    event.preventDefault();

    const url = document.location;
    const data = event.submitter.getAttribute('data-md-value');

    posthog.capture('feedback', { url: url.pathname, value: data });

    feedback.firstElementChild.disabled = true;
    const note = feedback.querySelector(".md-feedback__note [data-md-value='" + data + "']");
    if (note) {
      note.hidden = false;
    }
  });
});
