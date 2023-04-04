import numpy as np


####### peak score ###########
def peak_score_upperRight(peak_snippet, peak_length, background_length, pseudo_count=1):
    mid = len(peak_snippet) // 2
    peak_interior = pseudo_count + np.mean(
        peak_snippet[
            mid - peak_length : mid + peak_length, mid - peak_length : mid + peak_length
        ]
    )
    peak_background = pseudo_count + np.mean(
        peak_snippet[
            mid - background_length : mid - peak_length,
            mid + peak_length : mid + background_length,
        ]
    )

    return peak_interior / peak_background


def peak_score_lowerRight(peak_snippet, peak_length, background_length, pseudo_count=1):
    mid = len(peak_snippet) // 2
    peak_interior = pseudo_count + np.mean(
        peak_snippet[
            mid - peak_length : mid + peak_length,
            mid - peak_length : mid + peak_length,
        ]
    )
    peak_background = pseudo_count + np.mean(
        peak_snippet[
            mid + peak_length : mid + background_length :,
            mid + peak_length : mid + background_length,
        ]
    )

    return peak_interior / peak_background


def peak_score_upperLeft(peak_snippet, peak_length, background_length, pseudo_count=1):
    mid = len(peak_snippet) // 2
    peak_interior = pseudo_count + np.mean(
        peak_snippet[
            mid - peak_length : mid + peak_length,
            mid - peak_length : mid + peak_length,
        ]
    )
    peak_background = pseudo_count + np.mean(
        peak_snippet[
            mid - background_length : mid - peak_length,
            mid - background_length : mid - peak_length,
        ]
    )

    return peak_interior / peak_background


def peak_score_lowerLeft(peak_snippet, peak_length, background_length, pseudo_count=1):
    mid = len(peak_snippet) // 2
    peak_interior = pseudo_count + np.mean(
        peak_snippet[
            mid - peak_length : mid + peak_length,
            mid - peak_length : mid + peak_length,
        ]
    )
    peak_background = pseudo_count + np.mean(
        peak_snippet[
            mid + peak_length : mid + background_length :,
            mid - background_length : mid - peak_length,
        ]
    )

    return peak_interior / peak_background


def peak_score(peak_snippet, peak_length, background_length, pseudo_count=1):
    avg = (
        peak_score_upperRight(peak_snippet, peak_length, background_length)
        + peak_score_lowerRight(peak_snippet, peak_length, background_length)
        + peak_score_upperLeft(peak_snippet, peak_length, background_length)
        + peak_score_lowerLeft(peak_snippet, peak_length, background_length)
    ) / 4
    return avg


######### Tad score ########


def tad_score(contact_map, stall_list, index, delta, diag_offset, max_distance):
    """
    ----------------------
    Function tad_score(contact_map, stall_list, index, delta, diag_offset, max_distance)
    begin function

    set in_tad, out_tad, and adjacent matrices from tad_snippet_sectors function

    assert adjacent matrix to be in the shape of in_tad matrix

    return score as average of in_tad matrix over out_tad score:
           tad_score=np.mean(pile_center[in_tad]) / np.mean(pile_center[out_tad])

    end function
    ----------------------
    """
    in_tad, out_tad, pile_center = tad_snippet_sectors(
        contact_map, stall_list, index, delta, diag_offset, max_distance
    )
    assert pile_center.shape == (len(in_tad), len(in_tad))
    return np.mean(pile_center[in_tad]) / np.mean(pile_center[out_tad])


######## Flame scores #########
def flame_score_v(flame_snippet, flame_thickness, background_thickness):
    """
    vertical flame score
    """
    mid = (np.shape(flame_snippet)[1]) // 2 + 1
    return np.mean(
        avg_peaks[:, mid - flame_thickness // 2 : mid + flame_thickness // 2]
    ) / np.mean(
        avg_peaks[:, mid - background_thickness // 2 : mid + background_thickness // 2]
    )


def flame_score_h(flame_snippet, flame_thickness, background_thickness):
    """
    horizontal flame score
    """
    mid = len(flame_snippet) // 2 + 1
    return np.mean(
        flame_snippet[mid - flame_thickness // 2 : mid + flame_thickness // 2, :]
    ) / np.mean(
        avg_peaks[mid - background_thickness // 2 : mid + background_thickness // 2, :]
    )


######
