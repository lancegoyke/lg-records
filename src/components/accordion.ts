function accordion(querySelector: string) {
  const style = `
    .accordion-toggle { margin-bottom: 1rem; }
  `;
  const styleElement = document.createElement("style");
  styleElement.textContent = style;
  document.head.appendChild(styleElement);

  return document.querySelector(querySelector) as HTMLElement;
}

function accordionToggle(querySelector: string, accordionEl: HTMLElement) {
  const accordionToggleEl = document.querySelector(
    querySelector
  ) as HTMLElement;

  let visible = true;
  accordionToggleEl.addEventListener("click", () => {
    console.log("clicked");
    visible = !visible;
    accordionEl.classList.toggle("is-hidden");
    accordionToggleEl.textContent = visible ? "Hide" : "Show";
  });
}

export default function init(
  accordionElQuerySelector = ".accordion",
  accordionToggleElQuerySelector = ".accordion-toggle"
) {
  const accordionEl = accordion(accordionElQuerySelector);
  accordionToggle(accordionToggleElQuerySelector, accordionEl);
}
