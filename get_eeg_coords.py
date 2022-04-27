from eeg_positions import get_elec_coords, plot_coords

def get_eeg_coords():
  coords = get_elec_coords(
    system="1005",
    dim="2d",
  )
  return coords
