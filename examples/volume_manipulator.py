import napari
import numpy as np

from napari_threedee.manipulator.manipulator import VispyAxesOverlay

data = np.random.random((100, 100, 100))

viewer = napari.view_image(data)
image_layer = viewer.layers[0]

viewer.dims.ndisplay = 3

axis = VispyAxesOverlay(viewer=viewer, layer=image_layer)

napari.run()
