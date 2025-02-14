document$.subscribe(() => {
  const header = document.querySelector('[data-md-component="header"]');
  const tabs = document.querySelector('[data-md-component="tabs"]');
  const bundle = document.querySelector('[data-md-component="bundle"]');

  if (!header || !tabs) return;
  if (!bundle) {
    header.classList.remove('md-header--sticky');
    tabs.classList.remove('md-header--sticky');
    return;
  }

  let sticky = true;
  let ticking = false;

  const updateHeader = () => {
    sticky = window.scrollY > (sticky ? 0.6 : 0.7) * window.innerHeight;
    ticking = false;
    if (sticky !== header.classList.contains('md-header--sticky')) {
      header.classList.toggle('md-header--sticky', sticky);
      tabs.classList.toggle('md-header--sticky', sticky);
    }
  };

  const onScroll = () => {
    if (!ticking) {
      requestAnimationFrame(updateHeader);
      ticking = true;
    }
  };

  ['scroll', 'resize', 'touchmove', 'wheel'].forEach((event) => {
    window.addEventListener(event, onScroll, { passive: true });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
      onScroll();
    }
  });

  updateHeader();

  return () => {
    ['scroll', 'resize', 'touchmove', 'wheel'].forEach((event) => {
      window.removeEventListener(event, onScroll);
    });
    document.removeEventListener('keydown', onScroll);
  };
});
