import SwiftUI
import UIKit

/// The icon of a kind of drink — a copy of `DrinkIcon` in the app target;
/// the widget compiles separately and has the same pictures in its own
/// asset catalogue.
///
/// The drinks have their own full-colour pictures in the asset catalogue —
/// SF Symbols has a mug and a wine glass, but no flute, no shot glass and no
/// cocktail glass. Anything else (the custom drink's sliders, a name stored
/// before the pictures existed) is still an SF Symbol, so a name that is not
/// in the catalogue falls back to `Image(systemName:)`.
///
/// `size` is the font size the symbol used to be drawn at; the pictures get
/// a frame a little larger than that, because a glyph's visible height is
/// taller than its point size and the pictures carry some air in their box.
struct DrinkIcon: View {
    let name: String
    let size: CGFloat
    var weight: Font.Weight = .regular

    var body: some View {
        if UIImage(named: name) != nil {
            Image(name)
                .resizable()
                .scaledToFit()
                .frame(width: size * 1.45, height: size * 1.45)
        } else {
            Image(systemName: name)
                .font(.system(size: size, weight: weight))
        }
    }
}
