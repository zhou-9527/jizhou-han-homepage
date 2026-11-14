const filters = document.querySelectorAll('[data-filter]');
const groups = document.querySelectorAll('.paper-group');
for (const button of filters) {
  button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    for (const filter of filters) {
      filter.setAttribute('aria-pressed', String(filter === button));
    }
    for (const group of groups) {
      for (const paper of group.querySelectorAll('[data-kind]')) {
        paper.hidden = selected !== 'all' && paper.dataset.kind !== selected;
      }
      group.hidden = !group.querySelector('.paper:not([hidden])');
    }
  });
}
const languageLink = document.querySelector('.language');
languageLink.addEventListener('click', () => {
  languageLink.hash = location.hash;
});
