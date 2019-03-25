// Notebook Extension to allow singular Mode on Jupyter

define([
  'base/js/namespace',
  './chapel'
], function (Jupyter) {
  "use strict";

  return {
    load_ipython_extension: function () {
      console.log('Loading Chapel Mode...');
    }
  };

});