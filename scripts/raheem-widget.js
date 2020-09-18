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
    this.siteId = options.siteId || ''
    this.addWidget()
    this.addButton()
  }

  addWidget () {
    const iframeSrc = `https://5f64725ccfe63e0008315c3e--raheem-develop.netlify.app/widget/?siteId=${this.siteId}`
    $('body').append(
      `<iframe src="${iframeSrc}" height="500" width="360" frameborder="0" id="${this.widgetId}"></iframe>`
    );
    var frame = $(this.getSelector(this.widgetId))
    frame.css({
      'bottom': '50px',
      'opacity': '0',
      'position': 'fixed',
      'right': '70px',
      'transition': 'all .5s ease-in',
      'z-index': '-1000',
      'border-radius': '10px'
    })
  }

  addButton () {
    var self = this
    $('body').append(`<div id="${this.buttonId}">Show</div>`);

    $(this.getSelector(this.buttonId))
      .click(function () {
        self.showing = !self.showing
        $(self.getSelector(self.buttonId)).html(self.showing ? 'Hide' : 'Show')
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
        // 'color': 'white',
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
