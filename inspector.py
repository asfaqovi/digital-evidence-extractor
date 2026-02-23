from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_decimal_from_dms(dms, ref):
    """Helper to convert GPS degrees/minutes/seconds to decimal format."""
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        return -(degrees + minutes + seconds)
    else:
        return degrees + minutes + seconds

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            print(f"[-] No metadata found in {image_path}")
            return

        print(f"[*] Analyzing: {image_path}")
        print("-" * 30)

        # Iterate through tags
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)

            # Print standard data (Make, Model, Date)
            if tag_name in ['Make', 'Model', 'DateTime', 'Software']:
                print(f"{tag_name}: {value}")

            # Special handling for GPS Data
            if tag_name == 'GPSInfo':
                print("\n[+] GPS Data Found:")
                gps_data = {}
                for t in value:
                    sub_tag = GPSTAGS.get(t, t)
                    gps_data[sub_tag] = value[t]

                # Extract and Convert Lat/Long if available
                if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
                    lat = get_decimal_from_dms(gps_data['GPSLatitude'], gps_data['GPSLatitudeRef'])
                    long = get_decimal_from_dms(gps_data['GPSLongitude'], gps_data['GPSLongitudeRef'])
                    
                    print(f"    Latitude: {lat}")
                    print(f"    Longitude: {long}")
                    print(f"    Google Maps: https://www.google.com/maps?q={lat},{long}")
                else:
                    print("    (GPS coordinates present but incomplete)")

    except IOError:
        print(f"[!] Error: File {image_path} not found or not a valid image.")

if __name__ == "__main__":
    # CHANGE THIS to the path of your image
    target_image = "test_image.jpg" 

    extract_metadata(target_image) 
