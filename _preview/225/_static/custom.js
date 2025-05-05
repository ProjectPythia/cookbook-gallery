function getClassOfCheckedCheckboxes(checkboxes) {
  var tags = [];
  checkboxes.forEach(function (cb) {
    if (cb.checked) {
      tags.push(cb.getAttribute("rel"));
    }
  });
  return tags;
}

function change() {
  console.log("Change event fired.");
  var domainsCbs = document.querySelectorAll(".domains input[type='checkbox']");
  var eventsCbs = document.querySelectorAll(".events input[type='checkbox']");
  var packagesCbs = document.querySelectorAll(".packages input[type='checkbox']");

  var domainTags = getClassOfCheckedCheckboxes(domainsCbs);
  var eventTags = getClassOfCheckedCheckboxes(eventsCbs);
  var packageTags = getClassOfCheckedCheckboxes(packagesCbs);

  var filters = {
    domains: domainTags,
    events: eventTags,
    packages: packageTags
  };

  filterResults(filters);
}

function filterResults(filters) {
  console.log("Filtering results...");
  var rElems = document.querySelectorAll(".tagged-card");

  rElems.forEach(function (el) {
    var isVisible = true; // Assume visible by default

    // Check for matching domains
    if (filters.domains.length > 0) {
      var hasMatchingDomain = filters.domains.some(domain => el.classList.contains(domain));
      isVisible = isVisible && hasMatchingDomain;
    }

    // Check for matching events
    if (filters.events.length > 0) {
      var hasMatchingEvent = filters.events.some(event => el.classList.contains(event));
      isVisible = isVisible && hasMatchingEvent;
    }

    // Check for matching packages
    if (filters.packages.length > 0) {
      var hasMatchingPackage = filters.packages.some(package => el.classList.contains(package));
      isVisible = isVisible && hasMatchingPackage;
    }

    // Toggle visibility based on the result
    if (isVisible) {
      el.classList.remove("d-none");
      el.classList.add("d-flex");
    } else {
      el.classList.remove("d-flex");
      el.classList.add("d-none");
    }
  });

  // Update the margins after filtering
  updateMargins();
}

var checkboxes = document.querySelectorAll('input[type="checkbox"]');
checkboxes.forEach(function (checkbox) {
  checkbox.addEventListener("change", change);
});

function updateMargins() {
  const columns = document.querySelectorAll('.sd-col.sd-d-flex-row.docutils');

  columns.forEach(column => {
    // Check if this column has any visible cards
    const hasVisibleCard = Array.from(column.children).some(child => !child.classList.contains('d-none'));

    // Toggle a class based on whether there are visible cards
    if (hasVisibleCard) {
      column.classList.add('has-visible-card');
    } else {
      column.classList.remove('has-visible-card');
    }
  });
}

function clearCbs() {
  // Select all checkbox inputs and uncheck them
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(function(checkbox) {
    checkbox.checked = false;
  });

  change(); 
}

// Initial call to set up correct margins when the page loads
document.addEventListener('DOMContentLoaded', updateMargins);

console.log("Script loaded.");