/*
  How to use
  - Import JQuery
  - Import this file
  - Call `new RaheemWidget(options)` anywhere in your app
*/

class RaheemWidget {
  constructor (options) {
    // allow adding customizable options (id, class, size, label...)
    this.widgetId = options.iframeId || 'widget'
    this.buttonId = options.buttonId || 'add_widget'
    this.addWidget()
    this.addButton()
  }

  addWidget () {
    $('body').append(
      `<iframe src="https://raheem.org" height="500" width="300" frameborder="0" id="${this.widgetId}"></iframe>`
    );
    $(this.getSelector(this.widgetId)).css({
      'bottom': '50px',
      'opacity': '0',
      'position': 'fixed',
      'right': '50px',
      'transition': 'all .5s linear',
      'z-index': '-1000',
    })
  }

  addButton () {
    var self = this
    $('body').append(`<div id="${this.buttonId}">Show</div>`);

    $(this.getSelector(this.buttonId))
      .click(function () {
        self.showing = !self.showing
        $(self.getSelector(self.widgetId)).css({
          'opacity': self.showing ? 1 : 0,
          'z-index': self.showing ? 1000 : -1000
        })
      }).css({
        'align-items': 'center',
        'background': '#ffc107',
        'border-radius': '25px',
        'border': '0',
        'bottom': '0',
        'color': '#111',
        'cursor': 'pointer',
        'display': 'flex',
        'font-size': '14px',
        'height': '50px',
        'justify-content': 'center',
        'position': 'fixed',
        'right': '50px',
        'width': '50px',
      })
  }

  getSelector (id) {
    return `#${id}`
  }
}
